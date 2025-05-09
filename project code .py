from queue import Queue

def page_faults_extended(pages, n, capacity):
    frames = []
    indexes = Queue()
    page_fault_count = 0
    print("--- FIFO Page Replacement (Extended with Frame Tracking) ---")
    print("Page\tFrames")
    print("-" * 15)
    for page in pages:
        if page not in frames:
            page_fault_count += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                oldest_page = indexes.get()
                frames.remove(oldest_page)
                frames.append(page)
            indexes.put(page)
            print(f"{page}\t{frames}")
        else:
            print(f"{page}\t{frames} (Hit)")
    return page_fault_count

def page_faults_with_frames(pages, n, capacity):
    frames = []
    indexes = Queue()
    page_fault_count = 0
    frame_history = []
    for page in pages:
        if page not in frames:
            page_fault_count += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                oldest_page = indexes.get()
                frames.remove(oldest_page)
                frames.append(page)
            indexes.put(page)
        frame_history.append(list(frames))
    return page_fault_count, frame_history

def fifo_simulation(pages, capacities):
    results = {}
    for capacity in capacities:
        frames = []
        indexes = Queue()
        page_fault_count = 0
        for page in pages:
            if page not in frames:
                page_fault_count += 1
                if len(frames) < capacity:
                    frames.append(page)
                else:
                    oldest_page = indexes.get()
                    frames.remove(oldest_page)
                    frames.append(page)
                indexes.put(page)
        results[capacity] = page_fault_count
    return results

if __name__ == "__main__":
    pages = [7, 0, 1, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    n = len(pages)
    capacity = 4
    capacities_to_test = [2, 3, 4, 5, 6, 7]
    faults_extended = page_faults_extended(pages, n, capacity)
    print("\nTotal Page Faults:", faults_extended)
    faults_history, history = page_faults_with_frames(pages, n, capacity)
    print("\n--- FIFO Page Replacement (Returning Frame History) ---")
    print("Total Page Faults:", faults_history)
    print("Frame History:")
    for i, frame_state in enumerate(history):
        print(f"After page {pages[i]}: {frame_state}")
    fault_counts = fifo_simulation(pages, capacities_to_test)
    print("\n--- FIFO Simulation for Different Capacities ---")
    for capacity, faults in fault_counts.items():
        print(f"Capacity: {capacity}, Page Faults: {faults}")