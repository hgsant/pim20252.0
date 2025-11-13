
#include <stdio.h>

#ifdef _WIN32
#define API __declspec(dllexport)
#else
#define API
#endif

API float media(float n1, float n2, float n3) {
    return (n1+n2+n3)/3.0f;
}

API int situacao(float media, int faltas, int total_aulas) {
    float freq = 1.0f - ((float)faltas / (float)total_aulas);
    if (total_aulas <= 0) return 1;
    if (freq < 0.75f) return 0;
    if (media >= 6.0f) return 2;
    return 1;
}

API float normaliza(float n) {
    if (n < 0.0f) return 0.0f;
    if (n > 10.0f) return 10.0f;
    return n;
}
