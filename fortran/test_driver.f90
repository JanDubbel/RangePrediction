program original_lowtran_driver
 implicit none
 integer,parameter::nwl=68
 real::tx(nwl,63),vn(nwl),lam(nwl),trace(nwl),unif(nwl),suma(nwl),irrad(nwl,3),sumvv(nwl)
 real::z(1),p(1),t(1),w(12)
 integer::i
 z=0.;p=0.;t=0.;w=0.
 call lwtrn7(.false.,nwl,2000.0,3333.333,20.0,tx,vn,lam,trace,unif,suma,irrad,sumvv, &
             2,2,0,0,0,1,0,z,p,t,w,0.0,1.0,0.0,2.5)
 open(61,file='fortran_spectrum.csv',status='replace')
 write(61,'(a)') 'wn_cm,lambda_um,tau'
 do i=1,nwl
   if (vn(i)>0) write(61,'(f12.3,a,f14.8,a,f14.9)')vn(i),',',lam(i),',',tx(i,9)
 enddo
 close(61)
end program original_lowtran_driver
