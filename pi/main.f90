program main

    use pi, only: approximate_pi_fortran

    implicit none

    print *, "pi computed by fortran = ", approximate_pi_fortran(1000000)

end program
