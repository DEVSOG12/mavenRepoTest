import concurrent.futures
import time

def runMProcess(data, function):
    # Max number of processes = 4
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        # Start the load operations and mark each future with its data
        future_to_data = {executor.submit(function, item): item for item in data}
        for future in concurrent.futures.as_completed(future_to_data):
            item = future_to_data[future]
            try:
                result = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (item, exc))
            else:
                # Process the result as needed
                pass

def runMProcessWithReturn(data, function):
    results = []
    # Max number of processes = 4
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        # Start the load operations and mark each future with its data
        future_to_data = {executor.submit(function, item): item for item in data}
        for future in concurrent.futures.as_completed(future_to_data):
            item = future_to_data[future]
            try:
                result = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (item, exc))
            else:
                # Collect the results
                results.append(result)
    return results
