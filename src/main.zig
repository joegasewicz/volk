const std = @import("std");
const posix = std.posix;

pub fn main() !void {
    const fd = try posix.socket(
        posix.AF.INET,
        posix.SOCK.STREAM,
        posix.IPPROTO.TCP,
    );
    defer posix.close(fd);

    try posix.setsockopt(
        fd,
        posix.SOL.SOCKET,
        posix.SO.REUSEADDR,
        &std.mem.toBytes(@as(c_int, 1)),
    );

    var addr = posix.sockaddr.in{
        .family = posix.AF.INET,
        .port = std.mem.nativeToBig(u16, 8086),
        .addr = 0,                 // ← FIXED (0.0.0.0)
        .zero = .{0} ** 8,
    };

    try posix.bind(fd, @ptrCast(&addr), @sizeOf(@TypeOf(addr)));
    try posix.listen(fd, 128);

    std.debug.print("Listening on port 8080\n", .{});

    while (true) {
        const client = try posix.accept(fd, null, null, 0);
        defer posix.close(client);

        const response =
            "HTTP/1.1 200 OK\r\n" ++
                "Content-Type: text/plain\r\n" ++
                "Content-Length: 12\r\n" ++
                "Connection: close\r\n" ++
                "\r\n" ++
                "Hello Zig!\n";

        _ = try posix.write(client, response);
    }

}