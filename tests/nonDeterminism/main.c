#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * gitTimeStamp();

int main(int argc, char *argv[]) {

    char * timestamp = gitTimeStamp();

    if (timestamp == NULL) {
        printf("Failed to get timestamp\n");
        exit(1);
    }

    printf("The timestamp is: %s\n", timestamp);


    
    printf("Testing out the gitTimeStamp removing non-deteministic behavior\n");
    return 0;

}

char * gitTimeStamp() {
    char *  timestamp = NULL;
//   Run and get output of git log -1 --format=%ct 

    FILE *fp;
    char path[1035];

    /* Open the command for reading. */
    fp = popen("git log -1 --pretty='format:%cd' --date=format:'%Y-%m-%d %H:%M:%S'", "r");
    if (fp == NULL) {
        printf("Failed to run command\n" );
        return timestamp;
        // exit(1);
    }

    /* Read the output a line at a time - output it. */
    while (fgets(path, sizeof(path)-1, fp) != NULL) {
        timestamp = malloc(strlen(path) + 1);
        strcpy(timestamp, path);
    }

    /* close */
    pclose(fp);

    return timestamp;

}