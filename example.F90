module example

   implicit none
   private
   public fortran_dot

contains
   function fortran_dot(n, u, v) result(d) bind (c)

      use, intrinsic :: iso_c_binding, only: c_int, c_double

      integer(c_int), value :: n
      real(c_double)        :: u(*)
      real(c_double)        :: v(*)
      real(c_double)        :: d

      integer :: i

      d = 0.0d0
      do i = 1, n
         d = d + u(i)*v(i)
      end do

   end function
end module
