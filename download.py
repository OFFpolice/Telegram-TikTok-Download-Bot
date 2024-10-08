import yt_dlp
import aiohttp
import asyncio


async def download_video(url):
    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "outtmpl": "%(title)s.%(ext)s",
        "merge_output_format": "mp4",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                ydl = yt_dlp.YoutubeDL(ydl_opts)
                info_dict = await asyncio.to_thread(ydl.extract_info, url, download=True)
                video_path = ydl.prepare_filename(info_dict)
                description = info_dict.get("description", "")
                channel_url = info_dict.get("uploader_url", "")
                channel_name = info_dict.get("uploader", "")
                post_link = info_dict.get("webpage_url", "")
                return video_path, description, channel_url, channel_name, post_link
            else:
                return None
