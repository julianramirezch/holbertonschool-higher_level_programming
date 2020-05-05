#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: Pointer
 * Return: 0 is not palindrome , 1 if is palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *aux, *tmp;
	int cont = 0, cont2 = 0, cont3 = 0;
	int pal[2048];

	if (!head)
		return (0);
	aux = *head;
	if (!*head || aux->next == NULL)
		return (1);
	tmp = *head;
	while (tmp)
	{
		cont++;
		tmp = tmp->next;
	}

	for (cont2 = 0; cont2 < cont; cont2++)
	{
		pal[cont2] = aux->n;
		aux = aux->next;
	}
	cont--;
	while (cont > cont3)
	{
		if (pal[cont3] != pal[cont])
			return (0);
		cont3++;
		cont--;
	}

	return (1);
}
