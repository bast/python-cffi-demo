program main

    use pi, only: approximate_pi

    implicit none

    print *, "pi computed by fortran = ", approximate_pi(1000000)

end program
