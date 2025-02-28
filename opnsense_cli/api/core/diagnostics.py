from opnsense_cli.api.base import ApiBase


class Activity(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "activity"
    """
    Diagnostics ActivityController
    """

    @ApiBase._api_call
    def getActivity(self, *args):
        self.method = "get"
        self.command = "getActivity"


class Cpu_usage(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "cpu_usage"
    """
    Diagnostics Cpu_usageController
    """

    @ApiBase._api_call
    def getCPUType(self, *args):
        self.method = "get"
        self.command = "getCPUType"

    @ApiBase._api_call
    def stream(self, *args):
        self.method = "get"
        self.command = "stream"


class Dns(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "dns"
    """
    Diagnostics DnsController
    """

    @ApiBase._api_call
    def reverseLookup(self, *args):
        self.method = "get"
        self.command = "reverseLookup"


class Dns_diagnostics(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "dns_diagnostics"
    """
    Diagnostics Dns_diagnosticsController
    """

    @ApiBase._api_call
    def get(self, *args):
        self.method = "get"
        self.command = "get"

    @ApiBase._api_call
    def set(self, *args):
        self.method = "get"
        self.command = "set"

    @ApiBase._api_call
    def set(self, *args):
        self.method = "post"
        self.command = "set"


class Firewall(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "firewall"
    """
    Diagnostics FirewallController
    """

    @ApiBase._api_call
    def delState(self, *args):
        self.method = "post"
        self.command = "delState"

    @ApiBase._api_call
    def flushSources(self, *args):
        self.method = "post"
        self.command = "flushSources"

    @ApiBase._api_call
    def flushStates(self, *args):
        self.method = "post"
        self.command = "flushStates"

    @ApiBase._api_call
    def killStates(self, *args):
        self.method = "post"
        self.command = "killStates"

    @ApiBase._api_call
    def listRuleIds(self, *args):
        self.method = "get"
        self.command = "listRuleIds"

    @ApiBase._api_call
    def log(self, *args):
        self.method = "get"
        self.command = "log"

    @ApiBase._api_call
    def logFilters(self, *args):
        self.method = "get"
        self.command = "logFilters"

    @ApiBase._api_call
    def pfStates(self, *args):
        self.method = "get"
        self.command = "pfStates"

    @ApiBase._api_call
    def pfStatistics(self, *args):
        self.method = "get"
        self.command = "pfStatistics"

    @ApiBase._api_call
    def queryPfTop(self, *args):
        self.method = "post"
        self.command = "queryPfTop"

    @ApiBase._api_call
    def queryStates(self, *args):
        self.method = "post"
        self.command = "queryStates"

    @ApiBase._api_call
    def stats(self, *args):
        self.method = "get"
        self.command = "stats"

    @ApiBase._api_call
    def streamLog(self, *args):
        self.method = "get"
        self.command = "streamLog"


class Interface(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "interface"
    """
    Diagnostics InterfaceController
    """

    @ApiBase._api_call
    def CarpStatus(self, *args):
        self.method = "post"
        self.command = "CarpStatus"

    @ApiBase._api_call
    def delRoute(self, *args):
        self.method = "post"
        self.command = "delRoute"

    @ApiBase._api_call
    def flushArp(self, *args):
        self.method = "post"
        self.command = "flushArp"

    @ApiBase._api_call
    def getArp(self, *args):
        self.method = "get"
        self.command = "getArp"

    @ApiBase._api_call
    def getBpfStatistics(self, *args):
        self.method = "get"
        self.command = "getBpfStatistics"

    @ApiBase._api_call
    def getInterfaceConfig(self, *args):
        self.method = "get"
        self.command = "getInterfaceConfig"

    @ApiBase._api_call
    def getInterfaceNames(self, *args):
        self.method = "get"
        self.command = "getInterfaceNames"

    @ApiBase._api_call
    def getInterfaceStatistics(self, *args):
        self.method = "get"
        self.command = "getInterfaceStatistics"

    @ApiBase._api_call
    def getMemoryStatistics(self, *args):
        self.method = "get"
        self.command = "getMemoryStatistics"

    @ApiBase._api_call
    def getNdp(self, *args):
        self.method = "get"
        self.command = "getNdp"

    @ApiBase._api_call
    def getNetisrStatistics(self, *args):
        self.method = "get"
        self.command = "getNetisrStatistics"

    @ApiBase._api_call
    def getPfsyncNodes(self, *args):
        self.method = "get"
        self.command = "getPfsyncNodes"

    @ApiBase._api_call
    def getProtocolStatistics(self, *args):
        self.method = "get"
        self.command = "getProtocolStatistics"

    @ApiBase._api_call
    def getRoutes(self, *args):
        self.method = "get"
        self.command = "getRoutes"

    @ApiBase._api_call
    def getSocketStatistics(self, *args):
        self.method = "get"
        self.command = "getSocketStatistics"

    @ApiBase._api_call
    def getVipStatus(self, *args):
        self.method = "get"
        self.command = "getVipStatus"

    @ApiBase._api_call
    def searchArp(self, *args):
        self.method = "get"
        self.command = "searchArp"

    @ApiBase._api_call
    def searchNdp(self, *args):
        self.method = "get"
        self.command = "searchNdp"


class Lvtemplate(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "lvtemplate"
    """
    Diagnostics LvtemplateController
    """

    @ApiBase._api_call
    def addItem(self, *args):
        self.method = "post"
        self.command = "addItem"

    @ApiBase._api_call
    def delItem(self, *args):
        self.method = "post"
        self.command = "delItem"

    @ApiBase._api_call
    def get(self, *args):
        self.method = "get"
        self.command = "get"

    @ApiBase._api_call
    def getItem(self, *args):
        self.method = "get"
        self.command = "getItem"

    @ApiBase._api_call
    def searchItem(self, *args):
        self.method = "*"
        self.command = "searchItem"

    @ApiBase._api_call
    def set(self, *args):
        self.method = "post"
        self.command = "set"

    @ApiBase._api_call
    def setItem(self, *args):
        self.method = "post"
        self.command = "setItem"


class Netflow(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "netflow"
    """
    Diagnostics NetflowController
    """

    @ApiBase._api_call
    def cacheStats(self, *args):
        self.method = "get"
        self.command = "cacheStats"

    @ApiBase._api_call
    def getconfig(self, *args):
        self.method = "get"
        self.command = "getconfig"

    @ApiBase._api_call
    def isEnabled(self, *args):
        self.method = "get"
        self.command = "isEnabled"

    @ApiBase._api_call
    def reconfigure(self, *args):
        self.method = "post"
        self.command = "reconfigure"

    @ApiBase._api_call
    def setconfig(self, *args):
        self.method = "get"
        self.command = "setconfig"

    @ApiBase._api_call
    def status(self, *args):
        self.method = "get"
        self.command = "status"


class Networkinsight(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "networkinsight"
    """
    Diagnostics NetworkinsightController
    """

    @ApiBase._api_call
    def getInterfaces(self, *args):
        self.method = "get"
        self.command = "getInterfaces"

    @ApiBase._api_call
    def getMetadata(self, *args):
        self.method = "get"
        self.command = "getMetadata"

    @ApiBase._api_call
    def getProtocols(self, *args):
        self.method = "get"
        self.command = "getProtocols"

    @ApiBase._api_call
    def getServices(self, *args):
        self.method = "get"
        self.command = "getServices"


class Packet_capture(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "packet_capture"
    """
    Diagnostics Packet_captureController
    """

    @ApiBase._api_call
    def download(self, *args):
        self.method = "get"
        self.command = "download"

    @ApiBase._api_call
    def get(self, *args):
        self.method = "get"
        self.command = "get"

    @ApiBase._api_call
    def macInfo(self, *args):
        self.method = "get"
        self.command = "macInfo"

    @ApiBase._api_call
    def remove(self, *args):
        self.method = "post"
        self.command = "remove"

    @ApiBase._api_call
    def searchJobs(self, *args):
        self.method = "get"
        self.command = "searchJobs"

    @ApiBase._api_call
    def set(self, *args):
        self.method = "get"
        self.command = "set"

    @ApiBase._api_call
    def set(self, *args):
        self.method = "post"
        self.command = "set"

    @ApiBase._api_call
    def start(self, *args):
        self.method = "post"
        self.command = "start"

    @ApiBase._api_call
    def stop(self, *args):
        self.method = "post"
        self.command = "stop"

    @ApiBase._api_call
    def view(self, *args):
        self.method = "get"
        self.command = "view"


class Ping(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "ping"
    """
    Diagnostics PingController
    """

    @ApiBase._api_call
    def get(self, *args):
        self.method = "get"
        self.command = "get"

    @ApiBase._api_call
    def remove(self, *args):
        self.method = "post"
        self.command = "remove"

    @ApiBase._api_call
    def searchJobs(self, *args):
        self.method = "get"
        self.command = "searchJobs"

    @ApiBase._api_call
    def set(self, *args):
        self.method = "get"
        self.command = "set"

    @ApiBase._api_call
    def set(self, *args):
        self.method = "post"
        self.command = "set"

    @ApiBase._api_call
    def start(self, *args):
        self.method = "post"
        self.command = "start"

    @ApiBase._api_call
    def stop(self, *args):
        self.method = "post"
        self.command = "stop"


class Portprobe(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "portprobe"
    """
    Diagnostics PortprobeController
    """

    @ApiBase._api_call
    def get(self, *args):
        self.method = "get"
        self.command = "get"

    @ApiBase._api_call
    def set(self, *args):
        self.method = "get"
        self.command = "set"

    @ApiBase._api_call
    def set(self, *args):
        self.method = "post"
        self.command = "set"


class System(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "system"
    """
    Diagnostics SystemController
    """

    @ApiBase._api_call
    def memory(self, *args):
        self.method = "get"
        self.command = "memory"

    @ApiBase._api_call
    def systemDisk(self, *args):
        self.method = "get"
        self.command = "systemDisk"

    @ApiBase._api_call
    def systemInformation(self, *args):
        self.method = "get"
        self.command = "systemInformation"

    @ApiBase._api_call
    def systemMbuf(self, *args):
        self.method = "get"
        self.command = "systemMbuf"

    @ApiBase._api_call
    def systemResources(self, *args):
        self.method = "get"
        self.command = "systemResources"

    @ApiBase._api_call
    def systemSwap(self, *args):
        self.method = "get"
        self.command = "systemSwap"

    @ApiBase._api_call
    def systemTemperature(self, *args):
        self.method = "get"
        self.command = "systemTemperature"

    @ApiBase._api_call
    def systemTime(self, *args):
        self.method = "get"
        self.command = "systemTime"


class Systemhealth(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "systemhealth"
    """
    Diagnostics SystemhealthController
    """

    @ApiBase._api_call
    def getInterfaces(self, *args):
        self.method = "get"
        self.command = "getInterfaces"

    @ApiBase._api_call
    def getRRDlist(self, *args):
        self.method = "get"
        self.command = "getRRDlist"

    @ApiBase._api_call
    def getSystemHealth(self, *args):
        self.method = "get"
        self.command = "getSystemHealth"


class Traceroute(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "traceroute"
    """
    Diagnostics TracerouteController
    """

    @ApiBase._api_call
    def get(self, *args):
        self.method = "get"
        self.command = "get"

    @ApiBase._api_call
    def set(self, *args):
        self.method = "get"
        self.command = "set"

    @ApiBase._api_call
    def set(self, *args):
        self.method = "post"
        self.command = "set"


class Traffic(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "traffic"
    """
    Diagnostics TrafficController
    """

    @ApiBase._api_call
    def Interface(self, *args):
        self.method = "get"
        self.command = "Interface"

    @ApiBase._api_call
    def Top(self, *args):
        self.method = "get"
        self.command = "Top"

    @ApiBase._api_call
    def stream(self, *args):
        self.method = "get"
        self.command = "stream"

