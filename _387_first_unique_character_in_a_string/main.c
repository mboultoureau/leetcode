int firstUniqChar(char* s) {
    int count[26] = {0};
    int length = strlen(s);

    for (int i = 0; i < length; i++) {
        count[s[i] - 'a'] += 1;
    }
    
    for (int i = 0; i < length; i++) {
        if (count[s[i] - 'a'] == 1) {
            return i;
        }
    }

    return -1;
}