#include "lists.h"

/**
 * insert_node - a variable function that
 * inserts integer into sorted singly-linked list.
 * @head: variable pointer to head of linked list.
 * @number: a variable holding the number to insert.
 * Return: function fails return NULL.
 * else0 return0 pointer to new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(listint_t));

	if (node == NULL)
	{
		return (NULL);
	}

	node->n = number;

	if (*head == NULL || (*head)->n >= number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}

	listint_t *prev = *head;

	while (prev->next && prev->next->n < number)
	{
		prev = prev->next;
	}

	node->next = prev->next;
	prev->next = node;

	return (node);
}
