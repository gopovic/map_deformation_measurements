clear all;

load 'GMapping.mat';

% point 1
all21=[];
for i=1:size(GMapping_point1_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_point1_error(:,i));
   all21=[all21 [avg;limit]];
end

% point 2
all22=[];
for i=1:size(GMapping_point2_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_point2_error(:,i));
   all22=[all22 [avg;limit]];
end

% point 3
all23=[];
for i=1:size(GMapping_point3_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_point3_error(:,i));
   all23=[all23 [avg;limit]];
end

% point 4
all24=[];
for i=1:size(GMapping_point4_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_point4_error(:,i));
   all24=[all24 [avg;limit]];
end


% point 5
all25=[];
for i=1:size(GMapping_point5_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_point5_error(:,i));
   all25=[all25 [avg;limit]];
end

% point 6
all26=[];
for i=1:size(GMapping_point6_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_point6_error(:,i));
   all26=[all26 [avg;limit]];
end

% point 7
all27=[];
for i=1:size(GMapping_point7_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_point7_error(:,i));
   all27=[all27 [avg;limit]];
end

% point 8
all28=[];
for i=1:size(GMapping_point8_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_point8_error(:,i));
   all28=[all28 [avg;limit]];
end

% point 9
all29=[];
for i=1:size(GMapping_point9_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_point9_error(:,i));
   all29=[all29 [avg;limit]];
end



GMapping_points=[all21 all22 all23 all24 all25 all26 all27 all28 all29];

figure(1);
hold on
bar(1:45, GMapping_points(1,:))
errorbar(1:45, GMapping_points(1,:),GMapping_points(2,:),'.')
xlim([0 46]);
ylim([-0.1 1.6]);



load 'GMapping_wpm.mat';

% point 1
all21=[];
for i=1:size(GMapping_wpm_point1_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_wpm_point1_error(:,i));
   all21=[all21 [avg;limit]];
end

% point 2
all22=[];
for i=1:size(GMapping_wpm_point2_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_wpm_point2_error(:,i));
   all22=[all22 [avg;limit]];
end

% point 3
all23=[];
for i=1:size(GMapping_wpm_point3_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_wpm_point3_error(:,i));
   all23=[all23 [avg;limit]];
end

% point 4
all24=[];
for i=1:size(GMapping_wpm_point4_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_wpm_point4_error(:,i));
   all24=[all24 [avg;limit]];
end


% point 5
all25=[];
for i=1:size(GMapping_wpm_point5_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_wpm_point5_error(:,i));
   all25=[all25 [avg;limit]];
end

% point 6
all26=[];
for i=1:size(GMapping_wpm_point6_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_wpm_point6_error(:,i));
   all26=[all26 [avg;limit]];
end

% point 7
all27=[];
for i=1:size(GMapping_wpm_point7_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_wpm_point7_error(:,i));
   all27=[all27 [avg;limit]];
end

% point 8
all28=[];
for i=1:size(GMapping_wpm_point8_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_wpm_point8_error(:,i));
   all28=[all28 [avg;limit]];
end

% point 9
all29=[];
for i=1:size(GMapping_wpm_point9_error,2) 
   [avg, limit] =calculate_mean_and_limit(GMapping_wpm_point9_error(:,i));
   all29=[all29 [avg;limit]];
end



GMapping_wpm_points=[all21 all22 all23 all24 all25 all26 all27 all28 all29];

figure(2);
hold on
bar(1:45, GMapping_wpm_points(1,:))
errorbar(1:45, GMapping_wpm_points(1,:),GMapping_wpm_points(2,:),'.')
xlim([0 46]);
ylim([-0.1 1.6]);