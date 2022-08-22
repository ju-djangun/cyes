#include <stdio.h>
#include <stdlib.h>


void print_googoo() {
    for (int i=2; i<=9; i++) {
        for (int j=1; j<=9; j++) {
            printf("%d x %d = %d\n", i, j, (i*j));
        }
        printf("\n");
    }
}

int main(void) {
    printf("hello world!\n");
    print_googoo();

    return 0;
}
