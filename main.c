#include <stdio.h>
#include <string.h>
#include "stdbool.h"
#include "event.h"
#include "defs.h"

static void callback()
{
    printf("Call back fired...\n");
}

int main(void)
{
    char type[TYPE_LENGTH] = EV_TYPE_CALLBACK;
    struct Event myEvent = { .callback = &callback, .done = false };
    strcpy(myEvent.type, type);
    struct Event e = event_create(myEvent); // TODO push into linked list

    while (1)
    {
        if (strcmp(e.type, EV_TYPE_CALLBACK) == 0 && e.done == false)
        {
            e.callback();
            e.done = true;
        }
    }

    return 0;
}