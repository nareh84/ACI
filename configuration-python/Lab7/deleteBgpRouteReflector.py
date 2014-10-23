from cobra.model.bgp import RRNodePEp

from createBgpRouteReflector import input_key_args
from utility import *


def delete_bgp_route_reflector(modir, spine_id):

    # Query to the Route Reflector Node.
    bgp_rrnodepep = modir.lookupByDn('uni/fabric/bgpInstP-default/rr/node-' + spine_id)
    if isinstance(bgp_rrnodepep, RRNodePEp):
        bgp_rrnodepep.delete()
    else:
        print 'Spine Node', spine_id, 'has not been set as a Route Reflector Rode.'
        return

    print_query_xml(bgp_rrnodepep)
    commit_change(modir, bgp_rrnodepep)

if __name__ == '__main__':

    # Obtain the key parameters.
    try:
        key_args = [{'name': 'spine', 'help': 'Spine ID'}]
        host_name, user_name, password, args = set_cli_argparse('Delete a Bgp Route Reflector.', key_args)
        spine_id = args.pop('spine')

    except SystemExit:

        if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
            sys.exit('Help Page')

        host_name, user_name, password = input_login_info()
        spine_id = input_key_args()


    # Login to APIC
    modir = apic_login(host_name, user_name, password)

    # Execute the main function
    delete_bgp_route_reflector(modir, spine_id)

    modir.logout()

