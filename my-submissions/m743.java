
import java.awt.Point;

class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        boolean[] reached = new boolean[n + 1];
        reached[0] = true;

        HashMap<Integer, ArrayList<Point>> adj = new HashMap<>(n); 
        for (int[] time : times) {
            if (!adj.containsKey(time[0])) {
                adj.put(time[0], new ArrayList<Point>());
            }
            adj.get(time[0]).add(new Point(time[1], time[2]));
        }

        PriorityQueue<Point> pq = new PriorityQueue<>(20, (a, b) -> a.x - b.x);
        pq.add(new Point(0, k));

        int maxDelay = 0;
        while (!pq.isEmpty()) {
            Point curr = pq.poll();

            if (reached[curr.y]) {
                continue;
            }
            maxDelay = curr.x;
            reached[curr.y] = true;

            if (!adj.containsKey(curr.y))
                continue;
            for (Point nxt : adj.get(curr.y)) {
                if (!reached[nxt.x]) {
                    pq.add(new Point(curr.x + nxt.y, nxt.x));
                }
            }
        }

        for (boolean b : reached) {
            if (!b)
                return -1;
        }
        return maxDelay;

    }
}
