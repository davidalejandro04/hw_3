#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
double G  = (4*3.14159265358979323846*3.14159265358979323846);

int cantidadPlanetas(void);

void load_data(double cI[10][7]);

double calcularAceleracion(double cosax[10][7],int planeta,int c);

void actualizarMatriz(double actual[10][7],int p,double m,double x,double y,double z,double vx,double vy,double vz);

void copiar(double actual[10][7],double cI[10][7]);

void imprimirMatriz(double actual[10][7]);

int main()
{

	char *nombreArchivo;
	nombreArchivo="coordinates.csv";
	int N=cantidadPlanetas();

	double anterior[10][7];
	double actual[10][7];

	//Llena la matriz CI
	load_data(anterior);

	FILE *fout;
	fout=fopen("Datos.dat","w");
	
	//Guarda posiciones iniciales
	
	//Calcula primeras soluciones
	double t=0;
	double tfinal=255;
	double dt=1/(365.25);


	double factorMagico=1;

	{
		//imprimir inicial
		for (int i=0;i<10;i++)
		{	//t(0)
			fprintf(fout,"Planeta%d,%lf,%lf,%lf,%lf,%lf,%lf\n",i,anterior[i][1],anterior[i][2],anterior[i][3],anterior[i][4],anterior[i][5],anterior[i][6]);
					
		}

	
	}
	copiar(actual,anterior);

	
	
	{	double x_j,y_j,z_j,vx_j,vy_j,vz_j;
		

		for(t=t+dt;t<tfinal;t=t+dt)//t(2)
		{
			for(int i =0;i<10;i++)
			{	
				
				double vhalfx,vhalfy,vhalfz;

				vhalfx=anterior[i][4]+0.5*calcularAceleracion(anterior,i,1)*dt;
				vhalfy=anterior[i][5]+0.5*calcularAceleracion(anterior,i,2)*dt;
				vhalfz=anterior[i][6]+0.5*calcularAceleracion(anterior,i,3)*dt;
			
				x_j=anterior[i][1]+(vhalfx*dt);
				y_j=anterior[i][2]+(vhalfy*dt);
				z_j=anterior[i][3]+(vhalfz*dt);

				actual[i][1]=anterior[i][1]+(vhalfx*dt);
				actual[i][2]=anterior[i][2]+(vhalfy*dt);
				actual[i][3]=anterior[i][3]+(vhalfz*dt);
				

	//			printf("%d",i);
				vx_j=vhalfx+0.5*(calcularAceleracion(actual,i,1)*dt);
				vy_j=vhalfy+0.5*(calcularAceleracion(actual,i,2)*dt);
				vz_j=vhalfz+0.5*(calcularAceleracion(actual,i,3)*dt);
	
				fprintf(fout,"Planeta%d,%lf,%lf,%lf,%lf,%lf,%lf\n",i,x_j,y_j,z_j,vx_j,vy_j,vz_j);
				actualizarMatriz(actual,i,anterior[i][0],x_j,y_j,z_j,vx_j,vy_j,vz_j);
			}

			copiar(anterior,actual);


		}
	}
	fclose(fout);
}

void imprimirMatriz(double actual[10][7])
{
	for(int i=0;i<10;i++){
			printf("Planeta%d,%lf,%lf,%lf,%lf,%lf,%lf\n",i,actual[i][1],actual[i][2],actual[i][3],actual[i][4],actual[i][5],actual[i][6]);}
	
}

void copiar(double actual[10][7],double cI[10][7])
{
	int j=0;	
	while(j<10)
	{
		int i=0;
		while(i<7)
		{

			actual[j][i]=cI[j][i];
		i++;
		}
	j++;
	}

}

void actualizarMatriz(double a[10][7],int p,double m,double x,double y,double z,double vx,double vy,double vz)
{
	a[p][0]=m;
	a[p][1]=x;
	a[p][2]=y;
	a[p][3]=z;
	a[p][4]=vx;
	a[p][5]=vy;
	a[p][6]=vz;
}


double calcularAceleracion(double cosax[10][7],int planeta, int c)
{

	double aceleracion=0;
	double d,mag;
	double rix=cosax[planeta][1],riy=cosax[planeta][2],riz=cosax[planeta][3];
	double planetaj=0;
	
	for(int j=0;j<10;j++)
	{
		
		
		if(j!=planeta)
		{
			d=cosax[j][c]-cosax[planeta][c];
	
			mag=pow((cosax[j][1]-rix),2)+pow((cosax[j][2]-riy),2)+pow((cosax[j][3]-riz),2);
			mag=pow(mag,1.5);

			aceleracion=aceleracion+G*( (cosax[j][0]/cosax[0][0]) * d ) /mag;
		}
	}

	return aceleracion;
}


int cantidadPlanetas(void)
{
    int lines = 0, ch;
    FILE *file = fopen("coordinates.csv", "r");
    while(!feof(file))
    {
        ch = fgetc(file);
        if(ch == '\n')
        {
            lines++;
        }
    }
    return lines;
}



void load_data(double cI[10][7])
{

	char *delimiter=",";

	FILE* f = fopen("coordinates.csv", "r");

	char planeta[100];
	char * pch;
	int i;
	int j=0;
	while(fscanf(f, "%s",planeta)==1)
	{
		

			pch = strtok(planeta,",");

			i=0;
			while(i<7)
			{
				pch = strtok(NULL,",");
				cI[j][i]=atof(pch);
			i++;
			}
		j++;

	}


	fclose(f);

}

