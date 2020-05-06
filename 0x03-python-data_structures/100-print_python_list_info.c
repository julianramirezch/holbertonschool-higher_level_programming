#include <Python.h>

/**
 * print_python_list_info -  prints some basic info about Python lists.
 * @p: Python Object
 */

void print_python_list_info(PyObject *p)
{
	int j = 0, allocated;

	allocated = ((PyListObject *)p)->allocated;


	printf("[*] Size of the Python List = %zu\n", PyList_Size(p))
	printf("[*] Allocated = %zu\n", allocated);

	while (j < PyList_Size(p))
	{
		printf("Element %d: ", j)
		printf("%s\n"), Py_TYPE(PyList_GetItem(p, j))->tp_name);
		j++;
	}
}
