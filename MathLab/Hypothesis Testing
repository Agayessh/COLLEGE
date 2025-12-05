disp('Select the Hypothesis Test to perform:');
disp('1. Hypothesis Test for Population Mean');
disp('2. Hypothesis Test for Population Variance (Chi-square test)');
disp('3. Hypothesis Test for Population Proportion (Z-Test)');

testType1 = input('Enter your choice (1/2/3): ');

if testType1 == 1
    disp('   ');
    disp('----- HYPOTHESIS TEST FOR POPULATION MEAN -----')
    mu0 = input('Enter the hypothesized population mean (mu0): ');
    disp('Select the type of test:');
    disp('1. Left-tailed test (H1: mu < mu0)');
    disp('2. Right-tailed test (H1: mu > mu0)');
    disp('3. Two-tailed test (H1: mu ~= mu0)');
    testType2 = input('Enter your choice (1/2/3): ');
    sdKnown = input('Is the population standard deviation known? (1 = Yes, 0 = No): ');
    sampleData = input('Enter the sample data in vector form (e.g., [5 6 7 8 9]): ');

    if sdKnown == 1
        standDev = input('Enter the population standard deviation: ');
        test_use = "z-test";
    else
        test_use = "t-test";
    end

    sampSize = length(sampleData); % safer than manual entry
    alpha = input('Enter the level of significance (e.g., 0.05): ');
    xBar = mean(sampleData);
    s = std(sampleData);

    % Compute test statistic
    if sdKnown == 1
        z_comp = (xBar - mu0) / (standDev / sqrt(sampSize));
        t_comp = NaN;
    else
        t_comp = (xBar - mu0) / (s / sqrt(sampSize));
        z_comp = NaN;
    end

    % Determine critical value and p-value
    switch testType2
        case 1
            tail = "Left-tailed";
            if sdKnown == 1
                criticalValue = -norminv(1 - alpha);
                pValue = normcdf(z_comp);
            else
                criticalValue = -tinv(1 - alpha, sampSize - 1);
                pValue = tcdf(t_comp, sampSize - 1);
            end

        case 2
            tail = "Right-tailed";
            if sdKnown == 1
                criticalValue = norminv(1 - alpha);
                pValue = 1 - normcdf(z_comp);
            else
                criticalValue = tinv(1 - alpha, sampSize - 1);
                pValue = 1 - tcdf(t_comp, sampSize - 1);
            end

        case 3
            tail = "Two-tailed";
            if sdKnown == 1
                criticalValue = norminv(1 - alpha/2);
                pValue = 2 * (1 - normcdf(abs(z_comp)));
            else
                criticalValue = tinv(1 - alpha/2, sampSize - 1);
                pValue = 2 * (1 - tcdf(abs(t_comp), sampSize - 1));
            end
    end

    % Decision rule
    reject = false;
    if sdKnown == 1
        testValue = z_comp;
    else
        testValue = t_comp;
    end

    switch testType2
        case 1
            if testValue < criticalValue
                reject = true;
            end
        case 2
            if testValue > criticalValue
                reject = true;
            end
        case 3
            if abs(testValue) > criticalValue
                reject = true;
            end
    end

    % Display results
    disp(' ');
    disp('------------');
    fprintf('%-30s: %s\n', 'Type of Test', test_use);
    fprintf('%-30s: %0.3f\n', 'Level of Significance', alpha);
    fprintf('%-30s: %s\n', 'Kind of Test', tail);

    if sdKnown == 1
        fprintf('%-30s: %0.3f\n', 'Critical Value (z Critical)', criticalValue);
        fprintf('%-30s: %0.3f\n', 'Computed Value (z Computed)', z_comp);
    else
        fprintf('%-30s: %0.3f\n', 'Critical Value (t Critical)', criticalValue);
        fprintf('%-30s: %0.3f\n', 'Computed Value (t Computed)', t_comp);
    end

    fprintf('%-30s: %0.5f\n', 'p-value', pValue);

    if reject
        fprintf('%-30s: %s\n', 'Decision', 'Reject the null hypothesis.');
        fprintf('%-30s: %s\n', 'Conclusion', 'There is sufficient evidence to support the alternative hypothesis.');
    else
        fprintf('%-30s: %s\n', 'Decision', 'Fail to reject the null hypothesis.');
        fprintf('%-30s: %s\n', 'Conclusion', 'There is insufficient evidence to support the alternative hypothesis.');
    end
end

if testType1 == 2
    disp('   ');
    disp('----- HYPOTHESIS TEST FOR POPULATION VARIANCE -----')
    % Sample data as a vector
    sampleData = input('Enter sample data as vector: ');
    n = length(sampleData);
    sampleVar = var(sampleData);

    % Population Variance
    popu_Var = input('Enter the hypothesized population variance (𝜎02): '); % corrected typo

    % Picking of a test
    disp('Select the type of test:');
    disp('1. Two-tailed test ');
    disp('2. Left-tailed (σ2 < σ02)');
    disp('3. Right-tailed (σ2 > σ02)');
    testType3 = input('Enter your choice (1/2/3): ');
    alpha = input('Enter the level of significance (e.g., 0.05): ');

    % Chi Square Statistic
    chi2_stat = (n - 1) * sampleVar / popu_Var;
    switch testType3
        case 1 % Two-tailed
            chi2_low = chi2inv(alpha / 2, n - 1);
            chi2_high = chi2inv(1 - alpha / 2, n - 1);
            if chi2_stat < chi2_low || chi2_stat > chi2_high
                disp('Reject the null hypothesis');
            else
                disp('Fail to reject the null hypothesis');
            end

        case 2 % Left Tailed
            chi2_low = chi2inv(alpha, n - 1);
            disp('Left-tailed test selected:');
            disp(['Critical value: chi2_low = ', num2str(chi2_low)]);
            if chi2_stat < chi2_low
                disp('Reject the null hypothesis');
            else
                disp('Fail to reject the null hypothesis');
            end

        case 3 % Right Tailed
            chi2_high = chi2inv(1 - alpha, n - 1);
            disp('Right-tailed test selected:');
            disp(['Critical value: chi2_high = ', num2str(chi2_high)]);
            if chi2_stat > chi2_high
                disp('Reject the null hypothesis');
            else
                disp('Fail to reject the null hypothesis');
            end
    end
    % Display the test statistic
    disp(['Chi-square test statistic: ', num2str(chi2_stat)]);
end

if testType1 == 3
    disp('   ');
    disp('----- HYPOTHESIS TEST FOR POPULATION PROPORTION -----')
    x = input('Enter number of successes (x): ');
    n = input('Enter sample size (n): ');
    p0 = input('Enter hypothesized population proportion (Po): ');

    % Sample proportion
    p_hat = x / n;

    disp('Test Type:');
    disp('1. Two-tailed test');
    disp('2. Left-tailed (P < Po)');
    disp('3. Right-tailed (P > Po)');
    testType = input('Enter your choice (1/2/3): ');
    alpha = input('Enter the significance level (alpha): ');

    % Z Statistic
    Z = (p_hat - p0) / sqrt(p0 * (1 - p0) / n);

    % Critical Values
    Z_critical = norminv(1 - alpha / 2, 0, 1);
    Z_critical_left = norminv(alpha, 0, 1);
    Z_critical_right = norminv(1 - alpha, 0, 1);

    fprintf('\nSample Proportion (p̂): %.4f\n', p_hat);
    fprintf('Z Statistic: %.4f\n', Z);

    if testType == 1
        fprintf('Critical Z-value for two-tailed test: %.4f\n', Z_critical);
        if abs(Z) > Z_critical
            disp('Reject the null hypothesis');
        else
            disp('Fail to reject the null hypothesis');
        end
    elseif testType == 2
        fprintf('Critical Z-value for left-tailed test: %.4f\n', Z_critical_left);
        if Z < Z_critical_left
            disp('Reject the null hypothesis');
        else
            disp('Fail to reject the null hypothesis');
        end
    elseif testType == 3
        fprintf('Critical Z-value for right-tailed test: %.4f\n', Z_critical_right);
        if Z > Z_critical_right
            disp('Reject the null hypothesis');
        else
            disp('Fail to reject the null hypothesis');
        end
    end
end
