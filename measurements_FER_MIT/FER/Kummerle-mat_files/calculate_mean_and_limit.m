function [ avg, limit ] = calculate_mean_and_limit( vector )

    N=max(size(vector));
    
    avg=mean(vector);
    deviation=std(vector);
    
    %alpha=0.05
    limit=1.96*deviation/sqrt(N);
    
    


end

