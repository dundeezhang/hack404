export default function Tag({ tag }: { tag: string }) {
  return (
    <div
      className="rounded-xl border border-[#A9927D] px-2 py-1"
      style={{ fontFamily: "AlumniSans", fontWeight: 500 }}
    >
      <p className="text-[#A9927D] text-sm">{tag}</p>
    </div>
  );
}
