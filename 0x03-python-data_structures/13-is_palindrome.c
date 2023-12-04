#include "lists.h"
#include <stdlib.h>
#include <stdio.h>


/**
*add_nodeint - adds a new node at the beginning of a listint_t list
*@head: pointer to pointer of first node of listint_t list
*@n: integer to be included in new node
*Return: address of the new element, or NULL if it failed
*/

listint_t *add_nodeint(listint_t **head, const int n)
{
        listint_t *new;


        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = n;
        new->next = *head;
        *head = new;
        return (new);
}

/**
*is_palindrome - function to identify if single linked list is palindrome
*@head: pointer to pointer of first node of listint_t
*Return: 0 if not palindrome else 1
*/

int is_palindrome(listint_t **head)
{
        listint_t *head_new = *head;
        listint_t *mix = NULL, *mix_new = NULL;


        if (*head == NULL || head_new->next == NULL)
                return (1);
        while (head_new != NULL)
        {
                add_nodeint(&mix, head_new->n);
                head_new = head_new->next;
        }
        mix_new = mix;
        while (*head != NULL)
        {
                if ((*head)->n != mix_new->n)
                {
                        free_listint(mix);
                        return (0);
                }
                *head = (*head)->next;
                mix_new = mix_new->next;
        }
        free_listint(mix);
        return (1);
}
