#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: Pointer to head
 * @number: Integer
 * Return: Pointer
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux, *newn, *tmp;

	newn = malloc(sizeof(listint_t));
	if (newn == NULL)
		return (NULL);
	newn->n = number;
	newn->next = NULL;

	if (*head == NULL)
	{
		*head = newn;
		return (newn);
	}
	aux = *head;
	tmp = *head;
	if (number == aux->n)
	{
		newn->next = *head;
		*head = newn;
		return (newn);
	}
	while (aux)
	{
		aux = aux->next;
		if (aux->n > newn->n)
		{
			newn->next = aux;
			tmp->next = newn;
			return (newn);
		}
		if (aux->next == NULL)
		{
			aux->next = newn;
			return (newn);
		}
		tmp = tmp->next;
	}
return (free(newn), NULL);
}
