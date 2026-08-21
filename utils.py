import pandas as pd
import numpy as np
import os

class StormDataLoader:
    """Lớp thực hiện nhiệm vụ đọc dữ liệu từ nhiều nguồn/định dạng khác nhau (OOP & Exception Handling)"""
    
    def __init__(self, ibtracs_path: str):
        self.ibtracs_path = ibtracs_path

    def load_ibtracs_csv(self) -> pd.DataFrame:
        """Nguồn 1: Đọc dữ liệu bão IBTrACS từ file CSV"""
        try:
            if not os.path.exists(self.ibtracs_path):
                raise FileNotFoundError(f"Không tìm thấy file tại {self.ibtracs_path}")
            
            df = pd.read_csv(self.ibtracs_path, low_memory=False)
            print(f"✅ [Nguồn 1 - CSV] Đọc thành công dữ liệu bão IBTrACS: {len(df)} bản ghi.")
            return df
        except Exception as e:
            print(f"❌ Lỗi khi đọc file CSV IBTrACS: {e}")
            return pd.DataFrame()

    def load_damage_json(self) -> pd.DataFrame:
        """Nguồn 2: Đọc dữ liệu mô phỏng thiệt hại thiên tai/bão từ cấu trúc JSON/API"""
        try:
            json_data = [
                {"SEASON": 2020, "STORM_NAME": "LINFA", "REGION": "Mien Trung", "DAMAGE_BILLION_VND": 9500, "FATALITIES": 148},
                {"SEASON": 2020, "STORM_NAME": "MOLAVE", "REGION": "Mien Trung", "DAMAGE_BILLION_VND": 13200, "FATALITIES": 41},
                {"SEASON": 2020, "STORM_NAME": "GONI", "REGION": "Mien Trung", "DAMAGE_BILLION_VND": 550, "FATALITIES": 2},
                {"SEASON": 2021, "STORM_NAME": "CONSON", "REGION": "Mien Trung", "DAMAGE_BILLION_VND": 100, "FATALITIES": 2},
                {"SEASON": 2022, "STORM_NAME": "NORU", "REGION": "Mien Trung", "DAMAGE_BILLION_VND": 4100, "FATALITIES": 9}
            ]
            df_json = pd.DataFrame(json_data)
            print(f"✅ [Nguồn 2 - JSON/API] Đọc thành công dữ liệu thiệt hại: {len(df_json)} bản ghi.")
            return df_json
        except Exception as e:
            print(f"❌ Lỗi khi đọc dữ liệu JSON: {e}")
            return pd.DataFrame()


class StormAnalyzer:
    """Lớp xử lý tính toán, lọc và phân tích dữ liệu bão"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def filter_vietnam_region(self) -> pd.DataFrame:
        """Lọc bão khu vực Biển Đông & Việt Nam (Vĩ độ 6°N - 24°N, Kinh độ 102°E - 120°E)"""
        df_filtered = self.df[
            (self.df['LAT'] >= 6.0) & (self.df['LAT'] <= 24.0) & 
            (self.df['LON'] >= 102.0) & (self.df['LON'] <= 120.0)
        ].copy()
        return df_filtered

    def get_central_region_peak_months(self, df_vn: pd.DataFrame) -> pd.DataFrame:
        """Thống kê bão ảnh hưởng Miền Trung (Vĩ độ 11°N - 19°N) theo tháng"""
        df_central = df_vn[(df_vn['LAT'] >= 11.0) & (df_vn['LAT'] <= 19.0)]
        return df_central.groupby('MONTH')['SID'].nunique().reset_index()