"""
    This file is part of Delphi.

    Delphi is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Delphi is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Delphi.  If not, see <http://www.gnu.org/licenses/>.
"""

from environment import Environment
from netaddr import *

class Router:

    # Class constructor 
    # route => route dict of the config
    # environment => environment dict of the config
    # backends => the backend object of data resources
    def __init__(self, app, routes, environment, backends):
        self.environment_config = environment
        self.app = app
        self.route_config = routes
        self.environments = dict()
        self.routes = dict()
        self._buildEnvironments(backends)
        self._buildRouteTable()
        self.routeIndex = sorted(self.routes)

    # _buildEnvironments
    # Build the environments
    def _buildEnvironments(self, backends):
        print self.environment_config
        for env, desc in self.environment_config.iteritems():
            env_backend = []
            if type(desc['backend']) == type([]):
                for db in desc['backend']:
                    tmp = backends.getBackend(db)
                    if tmp is not None:
                        env_backend.append(tmp)
            else:
                tmp = backends.getBackend(desc['backend'])
                if tmp is not None:
                    env_backend.append(tmp)
            self.environments[env] = Environment(env, env_backend)

    # _buildRouteTable
    # The route table is for CIDR networks
    # If a path route is defined, the flask routing should
    # shortcut straight to the environment
    def _buildRouteTable(self):
        for name, route in self.route_config.iteritems():
            if route['type'] == 'path':
                self.app.add_url_rule(route['prefix'], view_func=self.environments[route['environment']].route(), methods=['GET', 'POST', 'PUT', 'DELETE'])
            elif route['type'] == 'cidr':
                self.routes[IPNetwork(route['source'])] = self.environments[route['environment']]

    def _findCIDR(self, addr):
        ip = IPAddress(addr)
        self.app.logger.debug("Searching for route from: {0}".format(ip))
        for net in self.routeIndex:
            self.app.logger.debug("Comparing CIDR {0} to Address {1}".format(ip, net))
            subnet = int(net.netmask) & int(net.ip)
            self.app.logger.debug("Subnet ({0}) & ({1}) == {2}".format(subnet, int(ip), subnet & int(ip)))
            if subnet & int(ip) == subnet:
                self.app.logger.debug("Match {0}".format(net))
                print "Match {0}".format(net)
                return net		

    # Route request
    def route(self, req):
       network = self._findCIDR(req.remote_addr)
       if network is not None:
           return self.routes[network]
       else:
           return None
