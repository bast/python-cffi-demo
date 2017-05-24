program main

    use, intrinsic :: iso_c_binding, only: c_double, c_int
    use pi, only: approximate_pi_fortran

    implicit none

    interface approximate_pi_c
!       function example_new() result(context) bind (c)
!           import :: c_ptr
!           type(c_ptr) :: context
!       end function
        function approximate_pi_c(num_points) bind (c)
            import :: c_double, c_int
            integer(c_int), value :: num_points
            real(c_double) :: approximate_pi_c
        end function
    end interface

    print *, "pi computed by fortran = ", approximate_pi_fortran(1000000)
    print *, "pi computed by c = ", approximate_pi_c(1000000)

end program
