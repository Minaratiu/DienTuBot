# actions/actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionTraCuuDiemChuanNam2025(Action):

    def name(self) -> Text:
        return "action_tra_cuu_diem_chuan_thpt_nam_2025"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text="Hãy cho tôi biết bạn muốn hỏi điểm chuẩn thpt của ngành nào?")
            return []
        diem_chuan_db = {
            "kỹ thuật điều khiển và tự động hóa": "26.19",
            "công nghệ kỹ thuật điện, điện tử": "24.61",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "25.5",
        }
        diem = diem_chuan_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm chuẩn thpt của ngành này.")
        dispatcher.utter_message(text=f"Điểm chuẩn thpt của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuMaNganhCuaKhoaKyThuatDienTu1(Action):
    def name(self) -> Text:
        return "action_tra_cuu_ma_nganh"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text="Hãy cho tôi biết bạn muốn hỏi mã ngành của ngành nào trong khoa Kỹ thuật điện tử 1?")
            return []
        ma_nganh_db = {
            "kỹ thuật điều khiển và tự động hóa": "7520216",
            "công nghệ kỹ thuật điện, điện tử": "7510301",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "7510301",
        }
        ma = ma_nganh_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về mã ngành của ngành này.")
        dispatcher.utter_message(text=f"Mã ngành của ngành {ten_nganh} là {ma} bạn nhé.")
        return []

class ActionTraCuuDiemTheoPhuongThucXetTuyenTaiNang(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_xet_tuyen_tai_nang"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển tài năng của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "82.35",
            "công nghệ kỹ thuật điện, điện tử": "66.2857",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "80.625",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển tài năng của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển tài năng của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoChungChiSAT(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_chung_chi_sat"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo chứng chỉ SAT của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "1397",
            "công nghệ kỹ thuật điện, điện tử": "1313.4285",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "1362.5",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo chứng chỉ SAT của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo chứng chỉ SAT của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoChungChiACT(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_chung_chi_act"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo chứng chỉ ACT của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "31.41",
            "công nghệ kỹ thuật điện, điện tử": "29.2685",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "30.375",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo chứng chỉ ACT của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo chứng chỉ ACT của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoBaiThiHSA(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_bai_thi_hsa"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo bài thi HSA của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "100.76",
            "công nghệ kỹ thuật điện, điện tử": "94.9057",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "98",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo bài thi HSA của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo bài thi HSA của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoChungChiTSA(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_bai_thi_tsa"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo chứng chỉ TSA của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "72.2228",
            "công nghệ kỹ thuật điện, điện tử": "67.8746",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "70.07",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo chứng chỉ TSA của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo chứng chỉ TSA của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoChungChiSPT(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_bai_thi_spt"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo chứng chỉ SPT của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "23.8075",
            "công nghệ kỹ thuật điện, điện tử": "21.9271",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "23.0313",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo chứng chỉ SPT của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo chứng chỉ SPT của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoChungChiAPT(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_bai_thi_apt"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo chứng chỉ APT của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "920.84",
            "công nghệ kỹ thuật điện, điện tử": "861.0341",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "896",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo chứng chỉ APT của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo chứng chỉ APT của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoXetTuyenKetHop(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_xet_tuyen_ket_hop"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo xét tuyển kết hợp của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "28.22",
            "công nghệ kỹ thuật điện, điện tử": "27.2928",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "27.875",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo xét tuyển kết hợp của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo xét tuyển kết hợp của ngành {ten_nganh} là {diem} bạn nhé.")
        return []
