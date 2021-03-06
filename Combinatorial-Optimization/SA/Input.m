function model=Input()
pos=[     74    65
          22    70
          42    47
          50    76
          30     3
          57    30
          27    84
         100    61
          69    83
          48    47
          13    35
          18    36
          10    61
           9    13
          77    40
          20    46
          11    36
          82    87
          43    19
          39    11
          84    27
          14    99
          35    41
          46    50
          93    32
          93    89
          81    17
          37    13
           5    80
          44    49
          38    17
          62    19
          30    69
          94    96
          52    19
           7    78
          83    53
          92     1
          94    81
          52    84
          33    74
           8    95
          10    66
          57    15
           1    50
          11    22
          66    48
          35    80
          27    18
          63    81]; 
    x=pos(:,1);
    y=pos(:,2);
    n=numel(x);
    D=zeros(n,n);
    for i=1:n-1
        for j=i+1:n
            D(i,j)=norm([x(i) y(i)]-[x(j) y(j)]);
            D(j,i)=D(i,j);
        end
    end
    model.D=D;
    model.pos=pos;
end