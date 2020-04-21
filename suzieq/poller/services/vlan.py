from suzieq.poller.services.service import Service


class VlanService(Service):
    """Vlan service. Different class because Vlan is not right type for EOS"""

    def clean_data(self, processed_data, raw_data):
        """CLeanup needed for the messed up MAC table entries in Linux"""

        if raw_data.get("devtype", None) == "eos":
            for entry in processed_data:
                if entry["pvid"] == 'None':
                    entry["pvid"] = 0

        return super().clean_data(processed_data, raw_data)
