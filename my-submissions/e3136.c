bool isValid(char* word) {
    bool cons = false;
    bool vow = false;
    int len = 0;

    while (*word) {
        len++;
        if (*word >= 65 && *word <= 90) {
            *word += 32;
        }

        // letter
        if (*word >= 97 && *word <= 122) {
            switch (*word) {
                case 'a' :
                case 'e' :
                case 'i' :
                case 'o' :
                case 'u' :
                    vow = true;
                    break;
                default :
                    cons = true;
                    break;
            }
            word++;
            continue;
        }

        if (*word >= 48 && *word <= 57) {
            word++;
            continue;
        }

        return false;
    }

    return cons && vow && (len >= 3);
}