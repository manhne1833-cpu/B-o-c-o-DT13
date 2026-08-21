"""
MODULE PHẦN MỀM PHÂN TÍCH DỮ LIỆU BÃO VỚI LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG (OOP)
Học phần: Lập trình Python cho Phân tích Dữ liệu
Đề tài: DT13 - Phân tích dữ liệu bão ảnh hưởng đến Việt Nam và Miền Trung
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium


class TyphoonDataLoader:
    """Lớp quản lý thu thập và tiền xử lý dữ liệu bão"""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None

    def load_and_clean(self) -> pd.DataFrame:
        """Đọc và làm sạch dữ liệu bão từ file CSV"""
        try:
            df = pd.read_csv(self.filepath)

            # Chuyển đổi định dạng thời gian
            df['ISO_TIME'] = pd.to_datetime(df['ISO_TIME'])

            # Xử lý ngoại lệ và lọc dữ liệu trùng/thiếu
            df = df.dropna(subset=['LAT', 'LON', 'WMO_WIND'])
            df = df.drop_duplicates()

            self.data = df
            print(f"[SUCCESS] Đã tải và làm sạch thành công {len(df)} bản ghi.")
            return self.data
        except Exception as e:
            print(f"[ERROR] Lỗi khi đọc dữ liệu ({type(e).__name__}): {e}")
            return None


class TyphoonAnalyzer:
    """Lớp thực hiện các phép phân tích thống kê và trực quan hóa"""

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def get_yearly_summary(self) -> pd.DataFrame:
        """Thống kê số lượng cơn bão và tốc độ gió trung bình theo năm"""
        summary = (
            self.df.groupby('YEAR')
            .agg(
                So_Luong_Bao=('SID', 'nunique'),
                Gio_Toi_Da_KMH=('WIND_KMH', 'max'),
                Ap_Suat_Thap_Nhat=('WMO_PRES', 'min'),
            )
            .reset_index()
        )
        return summary

    def plot_monthly_distribution(self, save_path=None):
        """Vẽ biểu đồ phân bố mùa bão theo tháng"""
        monthly = self.df.groupby('MONTH')['SID'].nunique().reset_index()
        plt.figure(figsize=(10, 5))

        # Đã cập nhật hue='MONTH' & legend=False để tránh cảnh báo Seaborn
        sns.barplot(
            data=monthly,
            x='MONTH',
            y='SID',
            hue='MONTH',
            palette='Blues_d',
            legend=False,
        )

        plt.title(
            'Phân bố số lượng các cơn bão theo tháng (Biển Đông & Việt Nam)',
            fontsize=14,
            fontweight='bold',
        )
        plt.xlabel('Tháng trong năm', fontsize=12)
        plt.ylabel('Số lượng cơn bão', fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        plt.show()

    def plot_storm_tracks_2d(self, storm_ids=None, save_path=None):
        """Vẽ quỹ đạo các cơn bão theo Kinh độ (LON) - Vĩ độ (LAT) bằng Scatter/Line plot"""
        plt.figure(figsize=(10, 8))

        # Nếu không truyền mã bão, mặc định vẽ 5 cơn bão đầu tiên
        if storm_ids is None:
            storm_ids = self.df['SID'].unique()[:5]

        plot_df = self.df[self.df['SID'].isin(storm_ids)].sort_values(
            ['SID', 'ISO_TIME']
        )

        sns.scatterplot(
            data=plot_df,
            x='LON',
            y='LAT',
            hue='SID',
            style='SID',
            s=50,
            zorder=3,
            palette='tab10',
        )
        sns.lineplot(
            data=plot_df,
            x='LON',
            y='LAT',
            hue='SID',
            legend=False,
            linewidth=1.5,
            alpha=0.7,
            palette='tab10',
        )

        plt.title(
            'Quỹ đạo các cơn bão theo Kinh độ - Vĩ độ',
            fontsize=14,
            fontweight='bold',
        )
        plt.xlabel('Kinh độ (Longitude - °E)', fontsize=12)
        plt.ylabel('Vĩ độ (Latitude - °N)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)

        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        plt.show()

    def plot_landfall_distribution(self, region_col='SUBBASIN', save_path=None):
        """Trực quan hóa phân bố điểm bão xuất hiện / đổ bộ theo Vùng (Region)"""
        if region_col not in self.df.columns:
            print(
                f"[WARNING] Không tìm thấy cột '{region_col}' trong dataset. Kiểm tra lại tên cột!"
            )
            return

        # Lấy điểm đầu tiên xuất hiện của mỗi cơn bão
        landfall_df = self.df.groupby('SID').first().reset_index()
        region_counts = landfall_df[region_col].value_counts().reset_index()
        region_counts.columns = [region_col, 'So_Luong']

        plt.figure(figsize=(10, 5))
        sns.barplot(
            data=region_counts,
            x=region_col,
            y='So_Luong',
            hue=region_col,
            palette='Reds_r',
            legend=False,
        )

        plt.title(
            'Phân bố số lượng bão theo Vùng / Phân khu',
            fontsize=14,
            fontweight='bold',
        )
        plt.xlabel('Khu vực / Vùng', fontsize=12)
        plt.ylabel('Số lượng cơn bão', fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        plt.show()

    def generate_track_map(self, storm_id: str, output_html='map_storm.html'):
        """Trực quan hóa quỹ đạo bão tương tác bằng Folium"""
        storm_df = self.df[self.df['SID'] == storm_id].sort_values('ISO_TIME')
        if storm_df.empty:
            print("[ERROR] Không tìm thấy mã bão trong dữ liệu!")
            return None

        m = folium.Map(
            location=[storm_df['LAT'].mean(), storm_df['LON'].mean()],
            zoom_start=6,
        )
        points = storm_df[['LAT', 'LON']].values.tolist()

        # Vẽ đường nối tọa độ
        folium.PolyLine(
            points,
            color='red',
            weight=3,
            opacity=0.8,
            popup=f"Bão {storm_df['NAME'].iloc[0]}",
        ).add_to(m)

        # Vẽ từng mốc tọa độ
        for _, row in storm_df.iterrows():
            folium.CircleMarker(
                location=[row['LAT'], row['LON']],
                radius=4,
                color='darkred',
                fill=True,
                popup=f"{row['ISO_TIME']} - Gió: {row['WIND_KMH']} km/h",
            ).add_to(m)

        m.save(output_html)
        print(f"[SUCCESS] Đã lưu bản đồ quỹ đạo bão tại: {output_html}")
