local playlist = {}

function scan_directory(directory)
    for file in lfs.dir(directory) do
        if file ~= "." and file ~= ".." then
            local path = directory .. "/" .. file
            local duration = mp.get_property_number("duration", 0, path)
            if duration ~= nil then
                table.insert(playlist, {path=path, name=file, duration=duration})
            end
        end
    end
end

function show_playlist()
    mpv_osd = mp.create_osd_overlay("ass-events")
    local ass = mp.get_property_osd("osd-ass-cc/0")
    local y = 50
    for i, item in ipairs(playlist) do
        local text = string.format("%d. %s (%.2f)", i, item.name, item.duration)
        ass = ass .. string.format("{\\an1\\pos(10,%d)\\bord2\\fs20\\c&HFFFFFF&\\3c&H000000&}%s", y, text)
        y = y + 30
    end
    mpv_osd.data = ass
    mp.set_osd_ass(0, 0, mpv_osd)
end

function play_item(index)
    if index >= 1 and index <= #playlist then
        localitem = playlist[index]
        mp.commandv("loadfile", item.path, "replace")
        mp.set_property("pause", "no")
    end
end

scan_directory("/path/to/folder")
show_playlist()

mp.add_key_binding("p", "show_playlist", function()
    show_playlist()
end)

mp.add_key_binding("1", "play_item1", function()
    play_item(1)
end)

mp.add_key_binding("2", "play_item2", function()
    play_item(2)
end)
