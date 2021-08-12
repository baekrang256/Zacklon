#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

//모범힌트 보지 않고 그냥 낸 답안이다.
//틀린건 아님. 잘 돌아간다.

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
                int L = i - 1, R = i + 1, U = j - 1, D = j + 1, count = 0; //범위 이탈하는지 확인하기 위해 만든 상수다. L은 Left, R은 Right, U는 Up, D는 Down. count는 횟수 세기 위해 만들었다.
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
