# Yahaan hum sabse majboot tareeke se video items ko dhoondhenge
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 1. Main List Container Dhoondhein
        main_list_wrapper = soup.find('div', class_='movieTrayWrapper') 
        
        if not main_list_wrapper:
            print("Error: Main video container 'movieTrayWrapper' not found.")
            return []
            
        # 🚨 FINAL CODE YAHAN HAI 🚨
        
        # 2. Container ke andar har video item ko dhoondhein
        # TAG: div | CLASS: slick-slide (Yeh abhi sabse stable hai)
        video_containers = main_list_wrapper.find_all('div', class_='slick-slide') 
        
        if not video_containers:
            print("Warning: Individual video items not found inside the tray.")
            
        # 3. Ab har item ke andar link dhoondhein
        for container in video_containers:
            # <a> tag ko dhoondhein (Line 53)
            # Maan lijiye link turant <a> tag mein hai
            a_tag = container.find('a', href=True) 
            
            # ... (Rest of the logic for extracting and appending link remains the same) ...
