import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import Link from "next/link";

export default function Home() {
	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Welcome"} />
			</PageHeader>
			<PageSection id={"about"}>
				<div>LLM Cocktail Book is ...</div>
			</PageSection>
			<PageSection id={"feature"}>
				<div>01 Chatbot</div>
				<Link href={"/chatbot"}>Click</Link>
			</PageSection>
		</Page>
	);
}
