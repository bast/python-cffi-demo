module pi

    implicit none

    public approximate_pi

    private

contains

    pure real(8) function distance_to_origin_squared(x, y)
        real(8), intent(in) :: x
        real(8), intent(in) :: y

        distance_to_origin_squared = x*x + y*y
    end function

    real(8) function approximate_pi(num_points)
        integer, intent(in) :: num_points

        integer :: i
        integer :: num_inside
        real(8) :: x
        real(8) :: y

        num_inside = 0

        do i = 1, num_points
            call random_number(x)
            call random_number(y)
            if (distance_to_origin_squared(x, y) < 1.0) then
                num_inside = num_inside + 1
            end if
        end do

        ! we multiply by 4 to get the full circle
        ! from the 4 segments
        approximate_pi = 4.0*num_inside/real(num_points)
    end function

end module
