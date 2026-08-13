#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include <inttypes.h>

#ifdef DEBUG
# define DEBUG_PRINT(x) printf x
#else
# define DEBUG_PRINT(x) do {} while (0)
#endif

#define D_MAX 1000ULL
#define MAX_SIZE 1000ULL


void print_problem(void) {
    puts(
        "# Problem 66: Diophantine Equation\n\n"
        "Consider quadratic Diophantine equations of the form:\n"
        "                   x^2 - D*y^2 = 1                   \n\n"
        "For example, when D=13, the minimal solution in x is \n"
        "                649^2 - 13*180^2 = 1.                \n\n"
        "It can be assumed that there are no solutions in positive\n"
        "integers when D is square. By finding minimal solutions\n"
        "in x for D = {2, 3, 5, 6, 7}, we obtain the following:\n\n"
        "                   3^2 - 2*2^2 = 1                   \n"
        "                   2^2 - 3*1^2 = 1                   \n"
        "                   9^2 - 5*4^2 = 1                   \n"
        "                   5^2 - 6*2^2 = 1                   \n"
        "                   8^2 - 7*3^2 = 1                   \n\n"
        "Hence, by considering minimal solutions in x for D<=7,\n"
        "the largest x is obtained when D=5. Find the value of\n"
        "D<=1000 in minimal solutions of x for which the largest\n"
        "value of x is obtained.\n\n"
    );
}

void print_explanation(void) {
    puts(
        "# Explanation: We can express each integer square root\n"
        "as a periodic continued fraction:\n"
        "          [a0; a1, a2, ..., a_{n-1}, 2*a0].          \n"
        "The fundamental solution of the Pell equation\n"
        "                   x^2 - D*y^2 = 1,                   \n"
        "is given by the k-th convergent fraction x/y of sqrt(D),\n"
        "where k:=n-1 when the period n is even, and k:=2*n-1\n"
        "when the period is odd.\n\n"
    );
}


typedef struct ContinuedFraction {
    uint64_t coefficients[MAX_SIZE];
    size_t period;
} ContinuedFraction;


ContinuedFraction sqrt_continued_fraction(const uint64_t N) {
    ContinuedFraction result;
    const uint64_t isqrtN = (uint64_t)sqrt(N);
    result.coefficients[0] = isqrtN;

    if (isqrtN * isqrtN == N) {
        result.period = 0;
        return result;
    }

    uint64_t an = isqrtN;

    uint64_t rem = 0;
    uint64_t div = 1;

    DEBUG_PRINT(("Expanding sqrt%"PRIu64":\n", N));

    for (size_t n=0; n<MAX_SIZE; n++) {
        an = (rem + isqrtN)/div;
        rem = an*div - rem;
        div = (N - rem*rem)/div;

        DEBUG_PRINT(("\ta%zu=%"PRIu64", next_fraction = (%"PRIu64"+sqrt%"PRIu64")/%"PRIu64"\n", n, an, rem, N, div));

        result.coefficients[n] = an;

        if (an == 2*isqrtN) {
            result.period = n;

            DEBUG_PRINT(("sqrt%"PRIu64" = [%"PRIu64"; ", N, isqrtN));
            for (size_t i=1; i<=result.period; i++) {
                if (i > 1) DEBUG_PRINT((", "));
                DEBUG_PRINT(("%"PRIu64, result.coefficients[i]));
            }
            DEBUG_PRINT(("]\nCoefficients repeat with period=%zu.\n", result.period));

            return result;
        }
    }

    fprintf(stderr, "Continued fraction period for N=%"PRIu64" exceeded MAX_SIZE (%lld).\n", N, MAX_SIZE);
    exit(EXIT_FAILURE);
}


void find_D_maximizing_x(void) {
    double max_x = 0;
    double y_maximizing_x = 0;
    uint64_t D_maximizing_x = 0;

    printf("The fundamental solutions when D<=%lld:\n\n", D_MAX);

	for (uint64_t D=2; D<=D_MAX; D++) {
	    ContinuedFraction cf = sqrt_continued_fraction(D);

	    if (cf.period == 0) continue;

        size_t end = (cf.period % 2 == 0) ? cf.period - 1 : 2*cf.period - 1;

        double pn = (double)cf.coefficients[0], pn_1 = 1.0;
        double qn = 1.0, qn_1 = 0.0;

        for (size_t n=0; n < end; n++) {
            double an = (double)cf.coefficients[1 + n%cf.period];
            double next_pn = an * pn + pn_1;
            pn_1 = pn;
            pn = next_pn;
            double next_qn = an * qn + qn_1;
            qn_1 = qn;
            qn = next_qn;
        }

        printf("%"PRIu64": %.0f^2 == %"PRIu64"*%.0f^2+1 == %.0f\n", D, pn, D, qn, D*qn*qn+1);

        if (pn > max_x) {
            max_x = pn;
            y_maximizing_x = qn;
            D_maximizing_x = D;
        }
	}
    printf("\nThe minimal solution (x,y)=(%.0f,%.0f) maximizing x is obtained for D=%"PRIu64".\n", max_x, y_maximizing_x, D_maximizing_x);
}


int main(void) {
    print_problem();
    print_explanation();
    find_D_maximizing_x();
	return 0;
}
