#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>

void numeroEsperadoDeClientesCola() {
	float lambda, wq;
	cout << "Tasa de medida de llegadas: " << endl;
	cin >> lambda;
	printf("Tiempo de espera en cola: ");
	cin >> wq;
	cout << "Clientes esperados en el sistema: " << lambda * wq << endl;
}


void numeroEsperadoDeClientesSistema() {
	float lambda, ws;
	cout << "Tasa de medida de llegadas: " << endl;
	cin >> lambda;
	cout << "Tiempo de espera en el sistema: " << endl;
	cin >> ws;
	cout << "Clientes esperados en el sistema: " << lambda * ws << endl;
}


void tiempoCola() {
	float m, wq, res;

	printf("Miu: ");
	scanf("%f", &m);
	printf("Tiempo de espera en la cola: ");
	scanf("%f", &wq);

	res = wq + (1 / m);
	printf("Clientes esperados en el sistema:  %f\n", res);
}

void clientesSistemaLambdaMiu() {
	float m, l, lq, res;

	printf("Miu: ");
	scanf("%f", &m);
	printf("Lambda: ");
	scanf("%f", &l);
	printf("Clientes en la cola: ");
	scanf("%f", &lq);

	res = lq + (l / m);

	printf("Clientes esperados en el sistema:  %f\n", res);
}

void mLs() {
	float l, m, res;

	printf("Lambda: ");
	scanf("%f", &l);
	printf("Miu: ");
	scanf("%f", &m);

	res = l / (m - l);
	printf("Clientes en el sistema: %f\n", res);
}

void mLq() {
	float l, m, res;

	printf("Lambda: ");
	scanf("%f", &l);
	printf("Miu: ");
	scanf("%f", &m);

	res = (l * l) / (m * (m - l));
	printf("Clientes en la cola: %f\n", res);
}


void mWs() {
	float l, m, res;

	printf("Lambda: ");
	scanf("%f", &l);
	printf("Miu: ");
	scanf("%f", &m);

	res = 1 / (m - l);
	printf("Espera en el sistema: %f\n", res);
}

void mWq() {
	float l, m, res;

	printf("Lambda: ");
	scanf("%f", &l);
	printf("Miu: ");
	scanf("%f", &m);

	res = l / (m * (m - l));
	printf("Espera en la cola: %f\n", res);
}

void pN() {
	float ro, n, res;

	printf("Ro: ");
	scanf("%f", &ro);
	printf("N: ");
	scanf("%f", &n);

	res = (1 - ro) * pow(ro, n);
	printf("Probabiliad: %f\n", res);
}

void PlsN() {
	float ro, n, res;

	printf("Ro: ");
	scanf("%f", &ro);
	printf("N: ");
	scanf("%f", &n);

	res = pow(ro, n + 1);
	printf("Probabiliad: %f\n", res);

}

void PwsT() {
	float ro, t, res, miu;

	printf("Ro: ");
	scanf("%f", &ro);
	printf("t: ");
	scanf("%f", &t);
	printf("miu: ");
	scanf("%f", &miu);

	res = pow(M_E, (-miu * (1 - ro) * t));
	printf("Probabiliad: %f\n", res);

}

void PwqT() {
	float ro, t, res, miu;

	printf("Ro: ");
	scanf("%f", &ro);
	printf("t: ");
	scanf("%f", &t);
	printf("miu: ");
	scanf("%f", &miu);

	res = ro * (pow(M_E, (-miu * (1 - ro) * t)));
	printf("Probabiliad: %f\n", res);

}

int main() {

	int opc;
	do {
		printf("\nOpciones:\nLEYES DE LITTLE\n1. Ls (clientes en sistema, usando L y Ws)\n2. Lq (clientes en la cola)\n3. Espera en la cola\n4. Ls (clientes en el sistema, usando L M y Lq\nM/M/1\n5. Ls (clientes en sistema)\n6. Lq (clientes en cola)\n7. Ws (espera en sistema)\n8. Wq (espera en cola)\n9. Pn\n10. P(Ls > n)\n11. P(Ws >t)\n12. P(Wq > t)\n13. Salir\n");
		scanf("%i", &opc);

		switch (opc) {
		case 1:
			clientesSistemaLambda();
			break;
		case 2:
			clientesCola();
			break;
		case 3:
			tiempoCola();
			break;
		case 4:
			clientesSistemaLambdaMiu();
			break;
		case 5:
			mLs();
			break;
		case 6:
			mLq();
			break;
		case 7:
			mWs();
			break;
		case 8:
			mWq();
			break;
		case 9:
			pN();
			break;
		case 10:
			PlsN();
			break;
		case 11:
			PwsT();
			break;
		case 12:
			PwqT();
			break;
		default:
			printf("No es opcion");
		}

	} while (opc != 13);

	return 0;
}