cdef extern from "volk.h":
    void volk()

cdef class Volk:

    def __cinit__(self):
        pass

    def run(self):
        volk()
