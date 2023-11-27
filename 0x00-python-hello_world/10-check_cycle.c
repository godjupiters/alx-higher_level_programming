#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: variable holding the head of the singly linked list.
 * Return: 0 if zero cycle, 1 if cycle exist.
 */

int check_cycle(listint_t *list) {
	listint_t *slow = list->next;
	listint_t *fast = list->next->next;

    if (list == NULL || list->next == NULL) {
	return (0);
    }

    while (slow && fast && fast->next) {
	if (slow == fast) {
		return (1);
	}

	slow = slow->next;
	fast = fast->next->next;
	}

	return (0);
}
