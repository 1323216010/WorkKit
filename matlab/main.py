import matlab.engine


eng = matlab.engine.start_matlab()
result = eng.sqrt(16.0)
print(result)  # 打印MATLAB sqrt函数的结果
eng.quit()
