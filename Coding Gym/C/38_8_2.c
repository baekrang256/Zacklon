#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

//모범 제안을 참고해서 만든 것이다.
//범위 벗어나는 조건들을 한 곳에 몰아서 continue 사용.
//그거 말고는 딱히 차이가 없다.

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
                int count = 0;

                for (int k = i - 1; k <= i + 1; k++)
                {
                    for (int l = j - 1; l <= j + 1; l++)
                    {
                        if (k < 0 || k >= m || l < 0 || l >= n)
                            continue;
                        else
                            if (Field[k][l] == '*')
                                count++;
                    }
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
