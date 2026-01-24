# Tello Simulation Stream (simuTelloStream)

Questo modulo permette di testare l'applicazione **Tello Stream** senza la necessità di un drone fisico. Utilizza una USB camera (webcam) come sorgente video e simula il comportamento del Tello tramite mockup.

Per garantire la massima fedeltà, il flusso video della webcam viene processato da **FFmpeg**, frapponendosi tra la camera e l'applicazione esattamente come avviene nella realtà con il flusso UDP del drone.

## Struttura del modulo

- `app_simuTelloStream.py`: L'applicazione Flask principale (versione simulata).
- `tello_manager_mockup.py`: Gestisce lo stato e la logica del drone simulato.
- `video_stream_decoder_mockup.py`: Utilizza FFmpeg per catturare la USB camera e restituire frame rawvideo BGR24.
- `wifi_utils_mockup.py`: Simula le operazioni di rete Wi-Fi.
- `config.yaml`: File di configurazione trasparente che separa le impostazioni di input tra Tello e Simulazione.
- `templates/index_simu.html`: Interfaccia web per il controllo della simulazione.

## Requisiti

1. **Python 3.x**
2. **OpenCV** (`pip install opencv-python`)
3. **Flask** (`pip install flask`)
4. **PyYAML** (`pip install pyyaml`)
5. **FFmpeg**: Deve essere presente nel sistema o nella cartella superiore come `ffmpeg.exe`.

## Guida all'utilizzo

### 1. Identificare la USB Camera
Prima di avviare, è necessario conoscere il nome che FFmpeg assegna alla tua webcam. Esegui il seguente comando in un terminale Windows:

```powershell
ffmpeg -list_devices true -f dshow -i dummy
```

Cerca nella sezione "DirectShow video devices" il nome della tua camera (es. `"Integrated Camera"` o `"USB Camera"`).

### 2. Configurazione
Apri `config.yaml` e imposta il nome della tua camera nella sezione `ffmpeg`:

```yaml
ffmpeg:
  # ...
  input_source: "video=NOME_DELLA_TUA_CAMERA"
```

### 3. Avvio
Esegui l'applicazione dedicata:

```powershell
cd simuTelloStream
python app_simuTelloStream.py
```

### 4. Utilizzo Browser
Apri il browser all'indirizzo `http://localhost:5000`. Segui la procedura standard:
1. Clicca **Connetti Wi-Fi** (verrà simulato il successo).
2. Clicca **Connetti Drone** (inizializzerà il mockup).
3. Attiva lo switch **Stream**. Il video apparirà nel riquadro, con un indicatore "SIMULAZIONE" sovraimpresso.

## Differenze Tecniche (Trasparenza)

L'applicazione è progettata per essere "agnostica" rispetto alla fonte. La differenza risiede esclusivamente nelle opzioni di input di FFmpeg gestite nel file di configurazione:

*   **Produzione (Tello Reale):** `Tello UDP → FFmpeg → rawvideo BGR24 → App`
*   **Simulazione (Questo modulo):** `USB Camera (dshow) → FFmpeg → rawvideo BGR24 → App`

Poiché le `output_options` di FFmpeg restano invariate, l'applicazione riceve fotogrammi con le stesse identiche caratteristiche in entrambi i contesti.


#### ESEMPI DI ELABORAZIONE IMMAGINE

Di seguito alcuni ESEMPI di elaborazione. Togli il commento (#) per attivarli uno alla volta. 
# --- SEZIONE DI ELABORAZIONE IMMAGINE (PERSONALIZZABILE) ------------------------------------------------
            #
            # Di seguito alcuni ESEMPI di elaborazione. Togli il commento (#) per attivarli uno alla volta.
            
            # --- ESEMPIO 1: Visione in Bianco e Nero ---
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR) # Riconvertiamo a 3 canali per poter disegnare testo colorato dopo
            
            # --- ESEMPIO 2: Rilevamento Bordi (Canny Edge Detection) ---
            # frame = cv2.Canny(frame, 100, 200)
            # frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR) # Necessario per compatibilità video
            
            # --- ESEMPIO 3: Disegna un Mirino al centro ---
            # h, w, _ = frame.shape
            # cx, cy = w // 2, h // 2
            # cv2.rectangle(frame, (cx - 50, cy - 50), (cx + 50, cy + 50), (0, 0, 255), 2)
            # cv2.line(frame, (cx - 60, cy), (cx + 60, cy), (0, 0, 255), 1)
            # cv2.line(frame, (cx, cy - 60), (cx, cy + 60), (0, 0, 255), 1)

            # --- ESEMPIO 4: Rilevamento Volti (Face Detection) ---

            
            #    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    
            #         # Usa detectMultiScale3 per ottenere i pesi (confidenza)
            #         faces, rejectLevels, levelWeights = self.face_cascade.detectMultiScale3(
            #             gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60), outputRejectLevels=True)
                    
            #         detected_faces = []
                    
            #         if len(faces) > 0:
            #             for (x, y, w_box, h_box), weight in zip(faces, levelWeights):
            #                 # Conversione euristica del peso in percentuale (peso * 10, max 100)
            #                 conf_pct = min(100, int(weight * 10))
                            
            #                 # Filtra solo se superiore al 60%
            #                 if conf_pct >= 60:
            #                     cv2.rectangle(frame, (x, y), (x+w_box, y+h_box), (255, 0, 0), 2)
            #                     cv2.putText(frame, f"Volto {conf_pct}%", (x, y-10), 
            #                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                                
            #                     detected_faces.append({
            #                         "x": int(x), "y": int(y), "w": int(w_box), "h": int(h_box), 
            #                         "confidence": int(conf_pct)
            #                     })
                    
            #         # Aggiungi i risultati al dizionario
            #         if detected_faces:
            #             results["faces"] = detected_faces


            
            # Usa i classificatori pre-addestrati inclusi in OpenCV
            # Nota: face_cascade viene inizializzato FUORI dal loop per performance (vedi riga 66)
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # # Parametri per rilevamento volti
            # faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
            
            # # NMS custom: elimina box sovrapposti mantenendo il più grande
            # def nms_faces(boxes, overlap_thresh=0.3):
            #     if len(boxes) == 0:
            #         return []
            #     # Converti in lista di tuple (x, y, w, h, area)
            #     boxes_with_area = [(x, y, w, h, w*h) for (x, y, w, h) in boxes]
            #     # Ordina per area decrescente (il più grande prima)
            #     boxes_with_area.sort(key=lambda b: b[4], reverse=True)
                
            #     keep = []
            #     while boxes_with_area:
            #         # Prendi il box più grande
            #         current = boxes_with_area.pop(0)
            #         keep.append(current[:4])  # Solo (x, y, w, h)
                    
            #         # Rimuovi box che si sovrappongono troppo
            #         remaining = []
            #         for box in boxes_with_area:
            #             # Calcola IoU (Intersection over Union)
            #             x1, y1, w1, h1 = current[:4]
            #             x2, y2, w2, h2 = box[:4]
                        
            #             # Coordinate di intersezione
            #             ix1 = max(x1, x2)
            #             iy1 = max(y1, y2)
            #             ix2 = min(x1+w1, x2+w2)
            #             iy2 = min(y1+h1, y2+h2)
                        
            #             # Area di intersezione
            #             iw = max(0, ix2 - ix1)
            #             ih = max(0, iy2 - iy1)
            #             intersection = iw * ih
                        
            #             # IoU = intersezione / unione
            #             union = w1*h1 + w2*h2 - intersection
            #             iou = intersection / union if union > 0 else 0
                        
            #             # Mantieni solo se sovrapposizione < soglia
            #             if iou < overlap_thresh:
            #                 remaining.append(box)
                    
            #         boxes_with_area = remaining
                
            #     return keep
            
            # # Applica NMS
            # faces = nms_faces(faces, overlap_thresh=0.3)
            
            # for (x, y, w_box, h_box) in faces:
            #     cv2.rectangle(frame, (x, y), (x+w_box, y+h_box), (255, 0, 0), 2)
            #     cv2.putText(frame, "Volto", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

            # --- ESEMPIO 5: Lettura QR Code ---
            # detector = cv2.QRCodeDetector()
            # data, bbox, _ = detector.detectAndDecode(frame)
            # if data:
            #     cv2.putText(frame, f"QR: {data}", (500, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
            #     if bbox is not None:
            #         # bbox è un array di punti 2D, serve convertirlo in int per polylines
            #         cv2.polylines(frame, [bbox.astype(int)], True, (0, 255, 0), 2)
            
        
        
     
            
        # Potresti aggiungere altri risultati qui
        # results["text_ocr"] = "..." 