#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list
 * Return: 0 is there no cycle , 1 if there is a cyle
 */

int check_cycle(listint_t *list)
{
	listint_t *aux = list;
	listint_t *tmp = list;

	if (!list || !list->next)
		return (0);

	aux = aux->next;
	tmp = tmp->next->next;

	while (aux && tmp && tmp->next)
	{
		if (aux == tmp)
			return (1);
		aux = aux->next;
		tmp = tmp->next->next;
	}
	return (0);
}
