function y=Muller(x0,x1,x2,eps,maxit)
    for iter=1:maxit
        h0=x1-x0;
        h1=x2-x1;
        d0=(f(x1)-f(x0))/h0;
        d1=(f(x2)-f(x1))/h1;
        a=(d1-d0)/(h1+h0);
        b=a*h1+d1;
        c=f(x2);
        rad=sqrt(b*b-4*a*c);
        if abs(b+rad)>=abs(b-rad)
            den=b+rad;
        else
            den=b-rad;
        end
        dxr=-2*c/den;
        xr=x2+dxr;
        fprintf("%d %g%+gi %g%+gi %g%+gi %g%+gi %g%+gi %g\n", iter,real(f(x2)),imag(f(x2)), real(a),imag(a),real(b),imag(b),real(c),imag(c), real(xr),imag(xr),abs(dxr)/xr);
        if abs(dxr)<eps*xr break
        end
        x0=x1;
        x1=x2;
        x2=xr;
    end
    y=xr;
end

function y=f(x)
    y=2*x^4+6*x^2+8;
end

z=Muller(-2,0,2,0.0001,20)