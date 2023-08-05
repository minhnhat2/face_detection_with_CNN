import cv2
import os

def capture_images(output_folder, num_images):
    # Kiểm tra nếu thư mục lưu trữ không tồn tại, tạo mới thư mục
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Khởi tạo camera
    cap = cv2.VideoCapture(0)

    # Đảm bảo camera đã sẵn sàng để sử dụng
    if not cap.isOpened():
        print("Không thể mở camera.")
        return

    try:
        for i in range(num_images):
            # Chụp ảnh từ camera
            ret, frame = cap.read()

            if not ret:
                print("Không thể chụp ảnh.")
                break

            # Resize ảnh thành kích thước 200x200
            resized_frame = cv2.resize(frame, (200, 200))

            # Chuyển đổi ảnh màu thành ảnh trắng đen
            grayscale_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

            # Lưu ảnh xuống thư mục
            image_filename = os.path.join(output_folder, f"image_{i + 1}.jpg")
            cv2.imwrite(image_filename, grayscale_frame)

            print(f"Đã chụp ảnh {i + 1}/{num_images}")

    except KeyboardInterrupt:
        print("Chương trình bị ngắt bởi người dùng.")

    # Giải phóng camera
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Đặt thư mục lưu trữ ảnh và số lượng ảnh muốn chụp
    output_folder = "/content/anh"  # Đổi đường dẫn này nếu muốn lưu ảnh vào thư mục khác
    num_images = 2000

    capture_images(output_folder, num_images)
