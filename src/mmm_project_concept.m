T=0.001;
t_total = 15;
t = 0:T:t_total;
N = length(t);
signal_length = 8;

omega = 10;
A = 1;
R1 = 1;
R2 = 1;
L = 1;
C = 1;

U = A.* sin(omega.*t);
%U = zeros(1,N);
%for i = 1:signal_length/T
%    U(i)=A;
%end
E = zeros(1,N);
UR = zeros(1,N);
SUM = 0;

a = 1 / R2 / C;
b = (R1 + R2)/R1/R2/C;

for i=1:N
    E(i) = U(i) - SUM.*b;
    SUM = SUM + E(i).* T;
    UR(i) = SUM * a;
end

figure(1) 
hold on; grid on;
%yyaxis left;
plot(t, U, 'r-');
%yyaxis right;
plot(t, UR, 'b-');

temp = -30:70;
omega_range = 10.^(temp.*0.1);
Amplification_Bode = a.*(b.^2 + omega_range.^2).^(-0.5);
Phaze_Bode = atan(-omega_range./b);

figure(2);
hold on; grid on;
set(gca, 'XScale', 'log')
plot(omega_range, Amplification_Bode , 'r-');

figure(3);
hold on; grid on;
set(gca, 'XScale', 'log')
plot(omega_range, Phaze_Bode , 'b-');