#include<stdio.h>

#define ARRAYSIZE 8
#define MAXNAMELENGTH 20

typedef struct employee
{
	char name[MAXNAMELENGTH];
	int ID;
	int age;
	float salary;
}EMPLOYEE;

typedef struct record
{
	EMPLOYEE employee;
	struct record* next;
}RECORD;

int main()
{
	initializeHashTables();
	while(1)
	{
		printf("Press 'A' to add an employee, 'B' to remove an employee, 'C' to search for employees meeting some criteria.");
		scanf("%c", &input);
		switch(input)
		{
			case('a'):
			case('A'):
				printf("You have chosen to add an employee.");
				EMPLOYEE* new_employee = (EMPLOYEE*) malloc(sizeof(EMPLOYEE));
				printf("Enter name: ");
				gets(new_employee->name);
				printf("Enter age: ");
				scanf("%d",&new_employee->age);
				printf("Enter salary: ");
				scanf("%f",&new_employee->salary);
				addEmployee(new_employee);
				break;
			case('b'):
			case('B'):
				printf("You have chosen to remove an employee.");
				printf("Enter the ID of the employee you want to remove: ");
				scanf("%d", &Id_to_remove);
				removeEmployee(id_to_remove);
				break;
			case('c'):
			case('C'):
				printf("You have chosen to search for employees meeting specific criteria.");
				printf("Enter name
			
