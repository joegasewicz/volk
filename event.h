//
// Created by Joe (Personal) on 23/12/2025.
//

#ifndef EVENT_H
#define EVENT_H

#include "stdbool.h"
#include "defs.h"

struct Event {
    char type[TYPE_LENGTH];
    void (*callback)();
    bool done;
};

struct Event event_create(struct Event e);

#endif //EVENT_H
