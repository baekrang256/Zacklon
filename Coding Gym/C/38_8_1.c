#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int m, n;

    scanf("%d %d", &m, &n);

    char** Field = malloc(sizeof(char *) * m);
    
    for (int i = 0; i < m; i++)
    {
        Field[i] = malloc(sizeof(char) * (n+1));
    }

    for (int i = 0; i < m; i++)
    {
        scanf("%s", Field[i]);
    }


    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (Field[i][j] == '*')
                printf("*");
            else
            {
                int L = i - 1, R = i + 1, U = j - 1, D = j + 1, count = 0;
                if (i == 0)
                    L += 1;
                if (i == m - 1)
                    R -= 1;
                if (j == 0)
                    U += 1;
                if (j == n - 1)
                    D -= 1;

                for (int k = L; k <= R; k++)
                    for (int l = U; l <= D; l++)
                    {
                        if (Field[k][l] == '*')
                            count++;
                    }
                printf("%d", count);

            }
        }
        printf("\n");
    }

    for (int i = 0; i < m; i++)
        free(Field[i]);

    free(Field);

    return 0;

}
