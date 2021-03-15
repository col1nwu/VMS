from pyroutelib3 import Router

router = Router("car")

start = router.findNode(41.8, -87.6)
end = router.findNode(41.4, -86.9)

status, route = router.doRoute(start, end)

if status == 'success':
    routeLatLons = list(map(router.nodeLatLon, route))
